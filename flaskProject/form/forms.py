from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField
from wtforms.validators import DataRequired

class StudentSurveyForm(FlaskForm):
    favorite_subject = RadioField('Кой е любимият ти предмет в училище?', choices=[
        ('math', 'Математика'),
        ('bulgarian', 'Български език и литература'),
        ('language', 'Чужд език'),
        ('it', 'Информатика / IT'),
        ('history', 'История / География'),
        ('science', 'Биология / Химия'),
        ('arts', 'Изкуства')
    ], validators=[DataRequired()])

    learning_style = RadioField('Как предпочиташ да учиш нови неща?', choices=[
        ('hands_on', 'Чрез практически задачи и опити'),
        ('listening', 'Слушайки и правейки записки'),
        ('reading', 'Четейки самостоятелно'),
        ('discussion', 'В група чрез дискусии и екипна работа')
    ], validators=[DataRequired()])

    strength = RadioField('Коя е най-силната ти страна?', choices=[
        ('logic', 'Логическо мислене и анализ'),
        ('communication', 'Комуникация и изразяване'),
        ('creativity', 'Креативност и въображение'),
        ('organization', 'Организация и самодисциплина'),
        ('tech', 'Работа с технологии')
    ], validators=[DataRequired()])

    future_study = RadioField('Какво искаш да учиш в бъдеще?', choices=[
        ('programming', 'Програмиране / ИТ'),
        ('humanities', 'Езици и хуманитарни науки'),
        ('sciences', 'Науки'),
        ('arts', 'Изкуства / Дизайн'),
        ('business', 'Бизнес и икономика'),
        ('undecided', 'Все още не съм сигурен/на')
    ], validators=[DataRequired()])

    class_behavior = RadioField('Как би описал/а себе си в класната стая?', choices=[
        ('active', 'Винаги съм активен участник'),
        ('thinker', 'Обичам да слушам и да разсъждавам'),
        ('helper', 'Помагам на другите'),
        ('independent', 'Предпочитам да работя самостоятелно')
    ], validators=[DataRequired()])

    activities = RadioField('Какви извънкласни дейности ти харесват най-много?', choices=[
        ('competitions', 'Състезания по математика, наука или програмиране'),
        ('journalism', 'Театър, писане, журналистика'),
        ('artistic', 'Музика, рисуване, танци'),
        ('volunteering', 'Доброволчество, ученически съвет'),
        ('sports', 'Спорт и физическа активност')
    ], validators=[DataRequired()])

    goal = RadioField('Какъв е твоят най-голям стремеж след училище?', choices=[
        ('abroad', 'Да уча в университет в чужбина'),
        ('career', 'Да започна кариера в конкретна област'),
        ('entrepreneur', 'Да създам собствен бизнес'),
        ('discover', 'Да открия какво ми е призванието'),
        ('helping', 'Да помагам на хората')
    ], validators=[DataRequired()])

    submit = SubmitField('Изпрати')
