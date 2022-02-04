from flask import Blueprint, render_template, request, redirect, url_for
from todo.extentions import mongo
from bson.objectid import ObjectId

main = Blueprint("main", __name__)

#todos is the name of the data base collection  

@main.route("/")
def index():
    todo_db = mongo.db.todos
    tasks = todo_db.find()
    return render_template("index.html", tasks=tasks)


@main.route("/add_item", methods=["POST"])
def add_item():
    if (request.form.get("item")):
        todo_item = request.form.get("item")
        
        todo_db = mongo.db.todos
        todo_db.insert_one({"task": todo_item, "status": False})

    return redirect(url_for("main.index"))

@main.route("/complete_todo<oid>")
def complete_todo(oid):
    todo_db = mongo.db.todos

    item = todo_db.find_one({"_id" : ObjectId(oid)})
    new_item = {"$set": { "status": True}}
    #item["status"] = True
    #todo_db.save_file(item)
    todo_db.update_one(item, new_item, upsert=False)
    return redirect(url_for("main.index"))

@main.route("/delete_completed", methods=["POST"])
def delete_completed():
    todo_db = mongo.db.todos
    todo_db.delete_many({"status": True})
    return redirect(url_for("main.index"))

@main.route("/delete_all", methods=["POST"])
def delete_all():
    todo_db = mongo.db.todos
    todo_db.delete_many({})
    return redirect(url_for("main.index"))
