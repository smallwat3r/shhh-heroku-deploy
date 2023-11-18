# Deploy Shhh on Heroku

[![Deploy][heroku-shield]][heroku]

Repository with required configurations to deploy [Shhh](https://github.com/smallwat3r/shhh) with Heroku on-click button.

Once deployed for the first time, you will need to initiate the database tables, which you can do with:

1. Access a Flask shell

        heroku run --app=<heroku-app-name> python3 -m flask shell

1. From the Flask shell, copy and run:

        from shhh.adapters import orm
        from shhh.extensions import db
        orm.metadata.create_all(db.engine)
        exit()

[heroku-shield]: https://www.herokucdn.com/deploy/button.svg
[heroku]: https://heroku.com/deploy?template=https://github.com/smallwat3r/shhh-heroku-deploy
