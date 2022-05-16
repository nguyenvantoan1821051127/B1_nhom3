# from crypt import methods
from app import app
from flask import render_template, request, redirect, flash, url_for, jsonify
from flask_login import current_user, login_user, logout_user, login_required

# from app import form
from app.models import *

from app.form import *


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/addstudent_s1")
@login_required
def addstudent_s1():
    if int(current_user.get_id()) != 1:
        flash('Only admin can access!')
        return redirect(url_for('index'))
    else:
        return render_template("addstudent_s1.html")


@app.route("/addstudent_s2", methods=["POST", "GET"])
def addstudent_s2():
    """add new student  """

    # Get form information.
    fullname = request.form.get("fullname")
    dob = request.form.get("dob")
    gender = request.form.get("gender")
    address = request.form.get("address")
    student = Student(fullname=fullname, dob=dob,
                      gender=gender, address=address)
    db.session.add(student)
    db.session.commit()
    return render_template("index.html")


# # ---------- Delete Student  ----------------


@app.route("/delete_student_s1")
@login_required
def delete_student_s1():
    if int(current_user.get_id()) != 1:
        flash('Only admin can access!')
        return redirect(url_for('index'))
    else:
        students = Student.query.all()
        return render_template("delete_student.html", students=students)


@app.route("/delete_student_s2", methods=["POST", "GET"])
def delete_student_s2():
    studentids = request.form.getlist('studentids')
    for studentid in studentids:
        student = Student.query.get(studentid)
        db.session.delete(student)
        db.session.commit()
    return render_template("index.html")

# ---------- update Student  ----------------


@app.route("/updatestudent_s1")
@login_required
def updatestudent_s1():
    students = Student.query.all()
    return render_template("updatestudent_s1.html", students=students)


@app.route("/updatestudent_s2/<int:studentid>")
def updatestudent_s2(studentid):
    # studentid = Student.query.get('studentid')
    students = Student.query.filter(Student.id == studentid).all()
    return render_template("updatestusent_s2.html", students=students)


@app.route("/updatestudent_s3", methods=["POST", "GET"])
def updatestudent_s3():
    student_id = int(request.form.get('student_id'))
    fullname = request.form.get("fullname")
    dob = request.form.get("dob")
    gender = request.form.get("gender")
    address = request.form.get("address")
    student = Student.query.get(student_id)
    student.fullname = fullname
    student.dob = dob
    student.gender = gender
    student.address = address
    db.session.commit()
    return render_template("index.html")


# ---------- sign up ----------------


@app.route("/wtf_singUp", methods=["GET", "POST"])
def wtf_singUp():
    """show sign up form"""

    form = signUpForm()
    if form.validate_on_submit():
        name = form.name.data
        password = form.password.data
        email = form.email.data
        Newuser = User(name=name, password=password,  email=email)
        Newuser.set_password(form.password.data)
        db.session.add(Newuser)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('index'))
    return render_template("wtf_signUp.html", form=form)
# ----------Login ----------------


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = loginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.name.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('nhap lai mat khau hoac tai khoan')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

# ---------- Logout ----------------


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

# ---------- Add new Teacher ----------------


@app.route("/addteacher_s1")
def addteacher_s1():
    return render_template("addteacher_s1.html")


@app.route("/addteacher_s2", methods=["POST", "GET"])
def addteacher_s2():
    """add new teacher  """

    fullname = request.form.get("fullname")
    phone = request.form.get("phone")
    gender = request.form.get("gender")
    email = request.form.get("email")
    teacher = Teacher(fullname=fullname, phone=phone,
                      gender=gender, email=email)
    db.session.add(teacher)
    db.session.commit()
    return render_template('index.html')


# ---------- Add new subjects ----------------
@app.route("/addsubject_s1")
@login_required
def addsubject_s1():
    """show all teacher"""
    if int(current_user.get_id()) != 1:
        flash('Only admin can access!')
        return redirect(url_for('index'))
    else:
        teachers = Teacher.query.all()
        return render_template("addsubject_s1.html", teachers=teachers)


@app.route("/addsubject_s2/<int:teacher_id>")
def addsubject_s2(teacher_id):
    """add new subject form"""

    teacher = Teacher.query.get(teacher_id)
    return render_template("addsubject_s2.html", teacher=teacher)


@app.route("/addsubject_s3", methods=["POST", "GET"])
def addsubject_s3():
    """commit add new subject"""

    # Get form information.
    teacher_id = int(request.form.get("teacher_id"))
    name = request.form.get("fullname")
    credit_number = request.form.get("credit_number")
    semester = request.form.get("semester")
    subject = Subject(teacher_id=teacher_id, name=name,
                      credit_number=credit_number, semester=semester)
    db.session.add(subject)
    db.session.commit()
    return render_template("index.html")

# ----------list all Subject  ----------------


@app.route("/searchsubject_s1")
def searchsubject_s1():
    """show all teacher"""
    teachers = Teacher.query.all()
    return render_template("searchsubject_s1.html", teachers=teachers)


@app.route("/searchsubject_s2/<int:teacher_id>")
def searchsubject_s2(teacher_id):
    """show all student"""
    teacher = Teacher.query.get(teacher_id)
    subjects = Subject.query.filter_by(teacher_id=teacher_id).all()
    return render_template("searchsubject_s2.html", teacher=teacher, subjects=subjects)


# ---------- Delete Subject  ----------------


@app.route("/delete_subject_s1")
@login_required
def delete_subject_s1():
    if int(current_user.get_id()) != 1:
        flash('Only admin can access!')
        return redirect(url_for('index'))
    else:
        subjects = Subject.query.all()
        return render_template("delete_subject.html", subjects=subjects)


@app.route("/delete_subject_s2", methods=["POST", "GET"])
def delete_subject_s2():
    subjectids = request.form.getlist('subject_ids')
    for subjectid in subjectids:
        subject = Subject.query.get(subjectid)
        db.session.delete(subject)
        db.session.commit()
    return render_template("index.html")


# ---------- Update Subject  ----------------


@app.route("/Update_subject_s1")
@login_required
def Update_subject_s1():
    teachers = Teacher.query.all()
    return render_template("update_subject_s1.html", teachers=teachers)


@app.route("/Update_subject_s2/<int:teacher_id>")
def Update_subject_s2(teacher_id):
    """add new daily flight form"""
    teacher = Teacher.query.get(teacher_id)
    subjects = Subject.query.filter(Subject.teacher_id == teacher_id).all()
    return render_template("update_subject_s2.html", subjects=subjects, teacher=teacher)


@app.route("/Update_subject_s3", methods=["POST", "GET"])
def Update_subject_s3():

    subject_id = int(request.form.get('subject_id'))
    name = request.form.get("name")
    semester = request.form.get("semester")
    credit_number = request.form.get("credit_number")
    teacher_id = int(request.form.get("teacher_id"))
    subject = Subject.query.get(subject_id)
    subject.teacher_id = teacher_id
    subject.name = name
    subject.semester = semester
    subject.credit_number = credit_number
    db.session.commit()
    return render_template("index.html")

# ---------- Update Subject  ----------------


@app.route("/filter_subject_s1")
@login_required
def filter_subject_s1():
    return render_template("filter_subject_s1.html")


@app.route("/filter_subject_s2", methods=["POST", "GET"])
def filter_subject_s2():
    name = request.form.get('fullname')
    if name is not None:
        students = Student.query.filter(Student.fullname == name).all()
    return render_template("delete_student.html", students=students)
