#!/usr/bin/env python
# Matt Van Veldhuizen
# 08/06/2015
# Udacity Full Stack Web Developer Nanodegree
# Implementation of a Conference Organization App
# providing a app to create, manage and join conferences
# main.py
# This Python code was based of the implementation
# by the teachers at Udacity.

"""
main.py -- Udacity conference server-side Python App Engine
    HTTP controller handlers for memcache & task queue access

$Id$

created by wesc on 2014 may 24

"""

__author__ = 'wesc+api@google.com (Wesley Chun)'

import webapp2
from google.appengine.api import app_identity
from google.appengine.api import mail
from conference import ConferenceApi

class SetAnnouncementHandler(webapp2.RequestHandler):
    def get(self):
        """Set Announcement in Memcache."""
        ConferenceApi._cacheAnnouncement()
        self.response.set_status(204)

class CheckFeaturedSpeakerHandler(webapp2.RequestHandler):
    def get(self):
        """Set FeaturedSpeaker in Memcache."""
        ConferenceApi._cacheFeaturedSpeaker()
        self.response.set_status(204)

class SendConfirmationEmailHandler(webapp2.RequestHandler):
    def post(self):
        """Send email confirming Conference creation."""
        mail.send_mail(
            'noreply@%s.appspotmail.com' % (
                app_identity.get_application_id()),     # from
            self.request.get('email'),                  # to
            'You created a new Conference!',            # subj
            'Hi, you have created a following '         # body
            'conference:\r\n\r\n%s' % self.request.get(
                'conferenceInfo')
        )

app = webapp2.WSGIApplication([
    ('/crons/set_announcement', SetAnnouncementHandler),
    ('/tasks/send_confirmation_email', SendConfirmationEmailHandler),
    ('/crons/check_featured_speaker', CheckFeaturedSpeakerHandler),
], debug=True)
