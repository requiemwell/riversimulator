#!/usr/bin/env python
# coding: UTF-8
#
## @package gender
#  the gender of animal
#  @author Wellington Oliveira
#  @since 23/02/2018

from enum import Enum


##
#   @param FEMALE is a type enum
#   @param MALE is a type enum
class Gender(Enum):
    FEMALE = 1
    MALE = 2
