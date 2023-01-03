from sqlalchemy.orm.session import Session
from db.models import Cars_DB


def add_car(db: Session, car_number):
    car = db.query(Cars_DB).filter(Cars_DB.car_number == car_number).first()
    if not car:
        new_car = Cars_DB(car_number=car_number)
        db.add(new_car)
        db.commit()
        db.refresh(new_car)
        return f"Car number {car_number} added!"
    else:
        detail = (f"Car number {car_number} already axist in the database",)
        return detail


def delete_car(db: Session, car_number):
    car = db.query(Cars_DB).filter(Cars_DB.car_number == car_number).first()
    if not car:
        detail = (f"Car number {car_number} do not exist in the database",)
        return detail

    else:
        db.delete(car)
        db.commit()
        detail = (f"Car number {car_number} has been deleted",)
        return detail
