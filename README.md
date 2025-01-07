# Deploy Shhh on Heroku

[![Deploy][heroku-shield]][heroku]

Repository with required configurations to deploy [Shhh](https://github.com/smallwat3r/shhh) with Heroku one-click button.

Once deployed you will need to run the database migrations, which you can do with:

        heroku run --app=<heroku-app-name> python3 -m flask db upgrade

[heroku-shield]: https://www.herokucdn.com/deploy/button.svg
[heroku]: https://heroku.com/deploy?template=https://github.com/smallwat3r/shhh-heroku-deploy
