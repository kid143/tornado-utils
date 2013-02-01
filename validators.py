#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2012 Kid143
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

'''Validators used for http request parameter validation.
   Validators are functions that validate request arguments.
   You can follow the instructions below to write your own validator:

   1. Validator function arguments begin with "value", which represent
      the request argument value, the following arguments are for the
      validation progress, which has no special requirements.
   2. There must be a message_info string in the arguments, which is
      used for error output.
   3. If the request argument value is valid, just return True, otherwise
      return a tuple (False, message_info)
'''

import re

def regex_validator(value, regex, message_info):
    '''use regex to test whether the value is matched'''
    matched = bool(re.match(regex, value, re.VERBOSE))
    
    return True if matched else (False, message_info)

def length_validator(value, length, mode ,message_info):
    '''validate the length of the parameter value.'''
    if mode == "longer":
        return True if len(value) >= length else (False, message_info)
    elif mode == "nolonger":
        return True if len(value) <= length else (False, message_info)
    else:
        print('Warning: mode not recognized, no validation has done.')
        return True

def email_validator(value, message_info='email address form not match'):
    '''validate email address.'''
    matched = bool(re.match(
        r'^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+((\.[a-zA-Z0-9_-]{2,3}){1,2})$', 
        value, re.VERBOSE))

    return True if matched else (False, message_info)

def required_validator(value, message_info='missing arguments.'):
    return True if not value or not value.strip() else (False, message_info)
