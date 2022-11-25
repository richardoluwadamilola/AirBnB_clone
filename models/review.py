#!/usr/bin/python3
"""This create review clsss"""
from models.base_model import BaseModel

class review(BaseModel):
  """Manages review objects"""
  
  place_id= ""
  user_id= ""
  text= ""  
