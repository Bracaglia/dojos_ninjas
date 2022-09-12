from flask_app import app, render_template, request, redirect
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/new/ninja')
def new_ninja():
    dojos = Dojo.get_all()
    return render_template('new_ninja.html',dojos = Dojo.get_all())


# ! CREATE 
@app.route('/create/ninja', methods = ['post'])
def create_ninja():
    print(request.form)
    ninja = Ninja.save(request.form)
    return redirect('/')

# ! READ ALL
@app.route('/ninjas')
def ninjas():
    return render_template('index.html', ninjas = Ninja.get_all())

# ! READ ONE
@app.route('/show/ninja/<int:id>')
def show_ninja(id):
    data = {'id': id}
    ninja = Ninja.get_one(data)
    dojo = Dojo.get_one({'id':ninja.dojo_id})
    return render_template('show_ninja.html', ninja = ninja)

# ! UPDATE
@app.route('/edit/<int:id>')
def edit_ninja(id):
    data = {'id':id}
    return render_template('edit_ninja.html', ninja = Ninja.get_one(data))

@app.route('/update/ninja', methods = ['post'])
def update_ninja():
    print(request.form)
    Ninja.update(request.form)
    return redirect(f"/show/{request.form['id']}")

# ! DELETE 
@app.route('/delete/<int:id>')
def delete_ninja(id):
    Ninja.destroy({'id': id})
    return redirect(f"/")