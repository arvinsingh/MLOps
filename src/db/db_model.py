"""
This module contains the SQLAlchemy model for the rent_apartments table.

The model is defined using SQLAlchemy's DeclarativeBase and Mapped classes.
Base is a subclass of DeclarativeBase, RentApartments is a subclass of Base.
Future models can be defined in a similar way.
"""

from sqlalchemy import INTEGER, REAL, VARCHAR
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from config import db_settings


class Base(DeclarativeBase):
    """
    Base class for the SQLAlchemy model.
    """

    pass


class RentApartments(Base):
    """
    rent_apartments table model for the SQLAlchemy ORM.

    Attributes:
        address (Mapped[str]): Address of the apartment.
        area (Mapped[float]): Area of the apartment.
        constraction_year (Mapped[int]): Year of construction of the apartment.
        rooms (Mapped[int]): Number of rooms in the apartment.
        bedrooms (Mapped[int]): Number of bedrooms in the apartment.
        bathrooms (Mapped[int]): Number of bathrooms in the apartment.
        balcony (Mapped[str]): Whether the apartment has a balcony.
        storage (Mapped[str]): Whether the apartment has storage.
        parking (Mapped[str]): Whether the apartment has parking.
        furnished (Mapped[str]): Whether the apartment is furnished.
        garage (Mapped[str]): Whether the apartment has a garage.
        garden (Mapped[str]): Whether the apartment has a garden.
        energy (Mapped[str]): Energy efficiency rating of the apartment.
        facilities (Mapped[str]): Additional facilities in the apartment.
        zip (Mapped[str]): ZIP code of the apartment.
        neighborhood (Mapped[str]): Neighborhood of the apartment.
        rent (Mapped[int]): Rent of the apartment.
    """

    __tablename__ = db_settings.rent_apart_table_name

    address: Mapped[str] = mapped_column(VARCHAR(), primary_key=True)
    area: Mapped[float] = mapped_column(REAL())
    constraction_year: Mapped[int] = mapped_column(INTEGER())
    rooms: Mapped[int] = mapped_column(INTEGER())
    bedrooms: Mapped[int] = mapped_column(INTEGER())
    bathrooms: Mapped[int] = mapped_column(INTEGER())
    balcony: Mapped[str] = mapped_column(VARCHAR())
    storage: Mapped[str] = mapped_column(VARCHAR())
    parking: Mapped[str] = mapped_column(VARCHAR())
    furnished: Mapped[str] = mapped_column(VARCHAR())
    garage: Mapped[str] = mapped_column(VARCHAR())
    garden: Mapped[str] = mapped_column(VARCHAR())
    energy: Mapped[str] = mapped_column(VARCHAR())
    facilities: Mapped[str] = mapped_column(VARCHAR())
    zip: Mapped[str] = mapped_column(VARCHAR())
    neighborhood: Mapped[str] = mapped_column(VARCHAR())
    rent: Mapped[int] = mapped_column(INTEGER())
