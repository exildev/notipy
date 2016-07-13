#!/usr/bin/env python
# -*- coding: utf-8 -*-
import models
import triggers
from connections import HOST, IO_PORT

class DefaultTrigger(triggers.Trigger):
    model = models.MyModel
    def save(self, instance):
        data = {
            'data':  {
                'data': 'data'
            }
        }
        self.emit('save', data)
    # end def
    def create(self, instance):
        data = {
            'data':  {
                'data': 'data'
            }
        }
        self.emit('create', data)
    # end def
    def update(self, instance):
        data = {
            'data': {
                'data': 'data'
            }
        }
        self.emit('update', data)
    # end def
# end class

class DefaultSMTPPlugin(triggers.TriggerSMTPPlugin):
    messages = {
        "save": {
            "headers": {
                "Subject": 'dato %(data)s'
            },
            "message_template": "notificaciones/email.html",
            "emails": ['luismiguel.mopa@gmail.com']
        },
        "create": {
            "headers": {
                "Subject": 'dato %(data)s'
            },
            "message_template": "notificaciones/email.html",
            "emails": ['luismiguel.mopa@gmail.com']
        },
        "update": {
            "headers": {
                "Subject": 'dato %(data)s'
            },
            "message_template": "notificaciones/email.html",
            "emails": ['luismiguel.mopa@gmail.com']
        }
    }
# end class

class DefaultIOPluing(triggers.TriggerIOPlugin):
    username = 'user2'
    password = '123456'
    host = HOST
    port = IO_PORT
# end class

triggers.triggers.register(DefaultTrigger, [DefaultIOPluing, DefaultSMTPPlugin])