#!/usr/bin/python3
"""This creates the review clsss"""
from models.base_model import BaseModel

class Review(BaseModel):
  """Manages review objects"""
  
  place_id= ""
  user_id= ""
  text= ""  
