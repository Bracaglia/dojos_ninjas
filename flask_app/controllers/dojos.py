from flask_app import app, render_template, request, redirect
from flask_app.models.dojo import Dojo


# ! CREATE 
@app.route('/create/dojo', methods = ['post'])
def create_dojo():
    print(request.form)
    dojo = Dojo.save(request.form)
    return redirect('/')

# ! READ ALL
@app.route('/')
def index():
    dojos = Dojo.get_all()
    ninjas_per_dojo = []
    for dojo in dojos:
        ninjas_per_dojo.append(Dojo.get_one_with_ninjas({'id': dojo.id}))

    return render_template('index.html', dojos = Dojo.get_all(), ninjas_per_dojo = ninjas_per_dojo)

# ! READ ONE
@app.route('/show/<int:id>')
def show_dojo(id):
    data = {'id': id}
    dojo = Dojo.get_one_with_ninjas(data)
    return render_template('show_dojo.html', dojo = dojo)

# ! UPDATE
@app.route('/edit/<int:id>')
def edit_dojo(id):
    data = {'id':id}
    return render_template('edit_dojo.html', dojo = Dojo.get_one(data))

@app.route('/update/dojo', methods = ['post'])
def update_dojo():
    print(request.form)
    Dojo.update(request.form)
    return redirect(f"/show/{request.form['id']}")

# ! DELETE 
@app.route('/delete/<int:id>')
def delete_dojo(id):
    Dojo.destroy({'id': id})
    return redirect(f"/")