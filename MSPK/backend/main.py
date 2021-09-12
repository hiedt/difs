import uvicorn
from fastapi import FastAPI
from database import curs


app = FastAPI()


@app.get("/employees")
async def get_employee(EmployeeId: int, offset: int=0, limit: int=10):
    curs.execute(
        "SELECT EmployeeId, LastName, FirstName, Title \
            FROM employees \
            WHERE EmployeeId=? \
            LIMIT ?, ?",
        (EmployeeId, offset, limit)
    )
    results = curs.fetchall()

    response = {
        "status_code": 200,
        "status": "Query successful",
        "results": results
    }
    return response


@app.get("/customers/{CustomerId}/invoices")
async def get_customer(CustomerId: int, offset: int=0, limit: int=10):
    curs.execute(
        "SELECT customers.CustomerId, FirstName, LastName, Phone, Email, Address, \
                InvoiceId, InvoiceDate, BillingCity \
            FROM customers \
            INNER JOIN invoices ON customers.CustomerId=invoices.CustomerID \
            WHERE customers.CustomerId=? \
            LIMIT ?, ?",
            (CustomerId, offset, limit)
    )
    results = curs.fetchall()

    response = {
        "status": "Query successful",
        "status_code": 200,
        "results_count": len(results),
        "results": results
    }

    return response


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) # port must be an integer
