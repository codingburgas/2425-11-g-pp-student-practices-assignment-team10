from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from . import form_bp
from .forms import StudentSurveyForm

@form_bp.route('/survey', methods=['GET', 'POST'])
@login_required
def survey():
    if current_user.role != 'student':
        flash("Само ученици имат достъп до анкетата.", "warning")
        return redirect(url_for('main.dashboard'))

    form = StudentSurveyForm()
    if form.validate_on_submit():
        #Записване на отговори (по-късно)
        return render_template('thank_you.html')

    return render_template('surveys/student_survey.html', form=form)
