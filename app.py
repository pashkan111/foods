from __init__ import create_app
from db import Food
from flask import render_template, request, redirect
from forms import FoodForm


app = create_app()

@app.route('/')
def index():
    foods = Food.get_all_food()
    for i in foods:
        print(i.razdel)
    return render_template(
        "index.html",
        title = 'Home',
        foods=foods,
    )


@app.route('/manage', methods=['POST', 'GET'])
def manage():
    if request.method=='POST':
        checked = request.form.getlist("checkbox")
        print(checked)
        foods = Food.get_all_food()
        for j in foods:
            if j.name in checked:
                j.is_active = True
                j.save_to_db()
            elif not j.name in checked:
                j.is_active = False
                j.save_to_db()     
    foods = Food.get_all_food()
    return render_template(
        "manage.html",
        title = 'Manage',
        foods=foods,
    )


@app.route('/create-food', methods=['POST', 'GET'])
def create_food():
    form = FoodForm(request.form)
    if request.method=="POST":    
        food = Food(**form.data)
        food.save_to_db()
        return redirect('/manage')
    return render_template(
        'form-create.html',
        form=form
    )


@app.route('/edit/<int:id>', methods=['POST', 'GET'])
def edit_food(id):
    form = FoodForm(request.form)
    if request.method=="POST":
        data = form.data
        for k, v in list(data.items()):
            if not v:
                data.pop(k)
        Food.edit_food(id=id, data=data)
        return redirect('/manage')
    return render_template(
        'form-edit.html',
        form=form
    )


if __name__ == '__main__':
    app.run(host='127.1.1.1', port=8100, debug=True)