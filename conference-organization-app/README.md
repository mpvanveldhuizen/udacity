# Conference Organization App API Project

### About

This project is a cloud-based API server to support a web-based application for conference organization.  The API supports the following functionality:

- User authentication (via Google accounts)
- User profiles
- Conference information
- Session information
- User wishlists

The API is hosted on [Google App Engine](https://developers.google.com/appengine) as application ID [project-4-1047](https://project-4-1047.appspot.com/#/), and can be accessed via the [API explorer](https://apis-explorer.appspot.com/apis-explorer/?base=https://project-4-1047.appspot.com/_ah/api#p/conference/v1/). This project was written in [Python](http://python.org/), using [Google Cloud Endpoints](https://developers.google.com/appengine/docs/python/endpoints/)

### Design and Improvement Tasks

#### Task 1: Add Sessions to a Conference

The following endpoint methods were added:

- `createSession`: given a conference, creates a session.
- `getConferenceSessions`: given a conference, returns all sessions.
- `getConferenceSessionsByType`: given a conference and session type, returns all applicable sessions.
- `getSessionsBySpeaker`: given a speaker, returns all sessions across all conferences.

The `Speaker` model design, was implemented using the following datastore properties:

| Property        | Type             |
|-----------------|------------------|
| name            | string, required |
| highlights      | string           |
| speaker         | string, required |
| duration        | integer          |
| typeOfSession   | string, repeated |
| date            | date             |
| startTime       | time             |
| organizerUserId | string           |

Parent-child implementation was used in order to represent the one `conference` to many `sessions` relationship.  This allows for strong consistent querying, as sessions can be queried by their conference ancestor.  While this remits the possibility to move sessions between conferences, the trade-off in speed and consistency was important.  Users would query about sessions quite often.  Sessions were `Memcached` to reflect that load.

In representing speakers, linking the speaker field to user profiles was determined not to be useful, as it would force a speaker to have an account, to be registered.  In other words, querying by speaker could produce undesirable results with inconsistent entry, e.g. "John Test, Johnny Test, J. Test" would all be listed as separate speakers.

Session types were implemented with sessions able to receive multiple different session types.

#### Task 2: Add Sessions to User Wishlist

The `Profile` model was modified to accommodate a wishlist stored as a repeated key property field, named `sessionsToAttend`.  In order to interact with this model in the API, previous methods from Task 1 were modified to return a unique web-safe key for sessions.  Two new endpoint methods were added to the API:

- `addSessionToWishlist`: given a session websafe key, saves a session to a user's wishlist.
- `getSessionsInWishlist`: return a user's wishlist.

#### Task 3: Indexes and Queries

Two endpoint methods were added for additional queries that would be useful for this application:

-`getConferenceSessionFeed`: returns a conference's sorted feed sessions occurring same day or later.
-`getTBDSessions`: returns sessions missing time/date information.

To implement the specialized query, finding non-workshop sessions before 7pm, was to first query sessions before 7pm with `ndb`, and then filter that list with Python to remove sessions with a 'workshop' type.

#### Task 4: Add Featured Speaker

The `createSession` endpoint was modified to cross-check if the speaker appeared in any other of the conference's sessions.  If so, the speaker name and relevant session names were added to the memcache under the `featured_speaker` key.  In addition a final endpoint, `getFeaturedSpeaker` was added, which would check the memcache for the featured speaker.  If empty, it would simply pull the next upcoming speaker.

### Setup Instructions

To deploy this API server locally, ensure that you have downloaded and installed the [Google App Engine SDK for Python](https://cloud.google.com/appengine/downloads). Once installed, conduct the following steps:

1. Clone this repository. Only the `conference-organization-app` directory is essential to this project.
2. (Optional) Update the value of `application` in `app.yaml` to the app ID you have registered in the App Engine admin console and would like to use to host your instance of this sample.
3. (Optional) Update the values at the top of `settings.py` to reflect the respective client IDs you have registered in the [Developer Console](https://console.developers.google.com/).
4. (Optional) Update the value of CLIENT_ID in `static/js/app.js` to the Web client ID
6. Run the app with the devserver using `dev_appserver.py DIR`, and ensure it's running by visiting your local server's address (by default [localhost:8080](localhost:8080).)
7. (Optional) Generate your client library(ies) with [the endpoints tool](https://developers.google.com/appengine/docs/python/endpoints/endpoints_tool).
8. (Optional) Deploy the application via `appcfg.py update`.