from pytorch_lightning.callbacks.progress.tqdm_progress import TQDMProgressBar
import torch
from pytorch_lightning import LightningModule, Trainer
from pytorch_lightning.loggers import MLFlowLogger
from torch import nn, random
from torch.nn import functional as F
from torch.utils.data import DataLoader, random_split
from torchmetrics.functional import accuracy
from torchvision import transforms
from torchvision.datasets import MNIST
import mlflow


class LitMNISTModel(LightningModule):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Flatten(),
            nn.Linear(1 * 28 * 28, 64),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Linear(32, 10),
        )

    def forward(self, x):
        x = self.model(x)
        return F.log_softmax(x, dim=1)

    def training_step(self, batch, batch_idx):
        x, y = batch
        loss = F.cross_entropy(self(x), y)
        self.log("train_loss", loss, prog_bar=True)

    def evaluate(self, batch, stage):
        x, y = batch
        loss = F.cross_entropy(logits := self(x), y)

        pred = torch.argmax(logits, dim=1)
        acc = accuracy(pred, y)

        if stage:
            self.log(f"{stage}_loss", loss, prog_bar=True)
            self.log(f"{stage}_acc", acc, prog_bar=True)

    def validate_step(self, batch, batch_idx):
        self.evaluate(batch, stage="val")

    def test_step(self, batch, batch_idx):
        self.evaluate(batch, stage="test")

    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters(), lr=0.02)


def create_datasets(transform):
    full = MNIST("data/", train=True, download=True, transform=transform)
    # Create data sets
    df_train, df_val = random_split(full, lengths=[55000, 5000])
    df_test = MNIST("data/", train=False, download=True, transform=transform)

    # Create dataloaders
    train_loader = DataLoader(
        dataset=df_train, batch_size=8, shuffle=True, num_workers=4
    )
    val_loader = DataLoader(
        dataset=df_val, batch_size=8, shuffle=True, num_workers=4
    )
    test_loader = DataLoader(
        dataset=df_test, batch_size=8, shuffle=True, num_workers=4
    )

    return train_loader, val_loader, test_loader


if __name__ == "__main__":
    mlflow.set_tracking_uri("mlflow_logs")
    mlflow.set_experiment('sample_mnist_lightningModule')  # set the experiment
    mlflow.pytorch.autolog()

    transform_pipeline = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,)),
    ])

    train_loader, val_loader, test_loader = create_datasets(transform_pipeline)

    model = LitMNISTModel()
    trainer = Trainer(
        accelerator="cpu",
        max_epochs=4,
        callbacks=[TQDMProgressBar(refresh_rate=30)],
        logger=False  # Disable Tensorboard logging
    )

    with mlflow.start_run() as run:
        trainer.fit(model, train_loader, val_loader)
        trainer.test(model, test_loader)
