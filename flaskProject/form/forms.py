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


class TeacherSurveyForm(FlaskForm):
    favorite_subjects_to_mentor = RadioField(
        'Which subject do you enjoy mentoring in the most?',
        choices=[
            ('math', 'Mathematics'),
            ('bulgarian', 'Bulgarian Language and Literature'),
            ('language', 'Foreign Languages'),
            ('it', 'Informatics / IT'),
            ('history', 'History / Geography'),
            ('science', 'Biology / Chemistry'),
            ('arts', 'Arts')
        ],
        validators=[DataRequired()]
    )

    teaching_style = RadioField(
        'What is your preferred teaching/mentoring style?',
        choices=[
            ('hands_on', 'Practical activities and demonstrations'),
            ('listening', 'Lectures and explanations'),
            ('reading', 'Assigning readings and discussion'),
            ('discussion', 'Collaborative discussions and teamwork')
        ],
        validators=[DataRequired()]
    )

    strengths = RadioField(
        'What is your strongest mentoring trait?',
        choices=[
            ('logic', 'Logical thinking and analysis'),
            ('communication', 'Communication and explanation'),
            ('creativity', 'Creativity and innovation'),
            ('organization', 'Structure and discipline'),
            ('tech', 'Using technology effectively')
        ],
        validators=[DataRequired()]
    )

    student_type_preference = RadioField(
        'What type of students do you work best with?',
        choices=[
            ('active', 'Highly active and engaged'),
            ('thinker', 'Reflective and thoughtful'),
            ('helper', 'Supportive and cooperative'),
            ('independent', 'Independent learners')
        ],
        validators=[DataRequired()]
    )

    extracurricular_focus = RadioField(
        'What kind of extracurricular mentoring do you enjoy most?',
        choices=[
            ('competitions', 'STEM competitions'),
            ('journalism', 'Writing, theatre, or journalism'),
            ('artistic', 'Music, art, or dance'),
            ('volunteering', 'Student council or volunteering'),
            ('sports', 'Sports and physical training')
        ],
        validators=[DataRequired()]
    )

    mentorship_goal = RadioField(
        'What is your primary goal as a mentor?',
        choices=[
            ('abroad', 'Help students apply abroad'),
            ('career', 'Guide toward specific careers'),
            ('entrepreneur', 'Support young entrepreneurs'),
            ('discover', 'Help them find their passion'),
            ('helping', 'Be a role model and helper')
        ],
        validators=[DataRequired()]
    )

    submit = SubmitField('Submit')