import flask, flask_wtf, wtforms, json


class Form(flask_wtf.FlaskForm):
    name = wtforms.StringField('ИМЯ')
    mail = wtforms.EmailField('МЫЛО')
    password = wtforms.PasswordField('КАКИЕ ТО ТОЧКИ')
    submit = wtforms.SubmitField('ДА Я ОТДАМ ВСЕ ИМУЩЕСТВО')


app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'DOPUSTIM'

@app.route('/', methods=['GET', 'POST'])
def register_view():
    form = Form()
    if flask.request.method == 'GET':
        return flask.render_template('pochta.html', form=form)

    name_data = form.name.data
    mail_data = form.mail.data
    pass_data = form.password.data

    user_data = [{'name': form.name.data,
                  'mail': form.mail.data,
                  'password': form.password.data}]

    with open('user_data.json', 'w') as file:
        json.dump(user_data, file, ensure_ascii=False)

    return f" {name_data} ОН ОТДАЛ ВСЕ ИМУЩЕСТВО , ЕГО МЫЛО {mail_data} , И ЕГО ТОЧКИ {pass_data}"


if __name__ == '__main__':
    app.run(debug=True)