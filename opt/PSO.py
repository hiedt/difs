import numpy as np

# Define the problem to be optimized (example: Sphere function)
def sphere_function(x):
    return np.sum(x**2)

# Define the PSO class
class ParticleSwarmOptimizer:
    def __init__(self, num_particles, num_dimensions, lower_bound, upper_bound):
        self.num_particles = num_particles
        self.num_dimensions = num_dimensions
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.particles = np.random.uniform(low=lower_bound, high=upper_bound, size=(num_particles, num_dimensions))
        self.velocities = np.zeros_like(self.particles)
        self.best_positions = self.particles.copy()
        self.best_fitness = np.array([sphere_function(p) for p in self.particles])
        self.global_best_position = self.best_positions[np.argmin(self.best_fitness)]
        self.global_best_fitness = np.min(self.best_fitness)
    
    def update_particles(self, inertia, cognitive_weight, social_weight):
        r1 = np.random.rand(self.num_particles, self.num_dimensions)
        r2 = np.random.rand(self.num_particles, self.num_dimensions)
        self.velocities = inertia * self.velocities + \
                           cognitive_weight * r1 * (self.best_positions - self.particles) + \
                           social_weight * r2 * (self.global_best_position - self.particles)
        self.particles += self.velocities
        
        new_fitness = np.array([sphere_function(p) for p in self.particles])
        update_indices = new_fitness < self.best_fitness
        self.best_positions[update_indices] = self.particles[update_indices]
        self.best_fitness[update_indices] = new_fitness[update_indices]
        
        if np.min(new_fitness) < self.global_best_fitness:
            self.global_best_position = self.particles[np.argmin(new_fitness)]
            self.global_best_fitness = np.min(new_fitness)
    
    def optimize(self, max_iterations, inertia, cognitive_weight, social_weight):
        for _ in range(max_iterations):
            self.update_particles(inertia, cognitive_weight, social_weight)
        return self.global_best_position

# Example usage
num_particles = 50
num_dimensions = 10
max_iterations = 100
inertia = 0.5
cognitive_weight = 2.0
social_weight = 2.0

pso = ParticleSwarmOptimizer(num_particles, num_dimensions, -10.0, 10.0)
solution = pso.optimize(max_iterations, inertia, cognitive_weight, social_weight)

print("Optimal solution found:", solution)
