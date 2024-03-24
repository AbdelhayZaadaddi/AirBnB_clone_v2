#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade="all,delete")
    else:
        name = ""

    @property
    def cities(self):
        """ Getter attribute to retrieve a list of cities"""
        from models import storage

        city_list = []
        for city_id, city_obj in storage.all(City).items():
            if city_obj.state_id == self.id:
                city_list.append(city_obj)
        return city_list
