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

import functools

def validate(field_config):
    '''This decorator is used for validating request parameters.
       Its design is inspired by the Annotated Validation framework
       from Struts2 in Java. You can write your own validator function
       to meet your own project requirements. For more info on 
       customized validator function, please refer to the docstring in
       validators module.
    '''
    def _validate(http_method_func):
        @functools.wraps(http_method_func)
        def __validate(self, *args, **kwargs):
            arguments = self.request.arguments
            self.logger.info('Validating requests...')
            error_info = []
            for name in field_config.keys():
                values = arguments.get(name, [])
                if len(values) > 0:
                    validators = field_config.get(name, [])
                    for value in values:
                        for validator in validators:
                            valid_state = None
                            try:
                                valid_state = validator[0](value, *validator[1])
                            except TypeError:
                                #if validator arguments are not provided
                                valid_state = validator(value)
                            if isinstance(valid_state, tuple):
                                assert isinstance(valid_state[1], str)
                                error_info.append({
                                            'fieldName': name,
                                            'value': value,
                                            'error_message': valid_state[1]
                                        })
            
            # You need a customized error page to output error info
            # This part can be modifed according to your requirements.
            if error_info:
                error_output = ''
                for error in error_info:
                    for key, value in error.items():
                        error_output += key
                        error_output += ': '
                        error_output += value
                        error_output += '<br/>'

                    error_output += '<br/>'

                self.dataModel={
                        'status_code': 400,
                        'err_info': error_output
                        }
                self.render('error.html', **self.dataModel)
                return

            #must use return so the function do not block in asynchronous mode.
            return http_method_func(self, *args, **kwargs)
        return __validate
    return _validate
