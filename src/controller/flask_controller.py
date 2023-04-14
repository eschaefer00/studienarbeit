import os
from urllib import request as req

from flask import Blueprint, request, flash, render_template, redirect, url_for, jsonify

from adapter.dall_e_2 import DallEAdapter
from adapter.deep_l import DeepLAdapter
from app.image_generator import ImageGenerator
from app.prompt_engineer import PromptEngineer

flask_controller = Blueprint("flask_controller", __name__)


@flask_controller.route("/", methods=["GET"])
def home():
    return render_template("home.html")


@flask_controller.route("/generateImage", methods=["POST"])
def enter_prompt():
    if request.method == 'POST':
        prompt = request.json.get("prompt")
        if len(prompt) < 1:
            flash('Please enter a proper prompt')
            return
        deep_l_adapter = DeepLAdapter(os.environ["DEEP_KEY"])
        prompt_engineer = PromptEngineer(deep_l_adapter)
        edited_prompt = prompt_engineer.define_art_style(prompt)
        dall_e_adapter = DallEAdapter(os.environ["API_KEY"])
        image_generator = ImageGenerator(dall_e_adapter)
        image_url = image_generator.generate_image(edited_prompt)
        req.urlretrieve(image_url, os.path.join("images", f"{prompt}.png"))
    else:
        flash('Wrong method')
        return
    return jsonify(imageUrl=image_url, prompt=prompt)
