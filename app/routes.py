from flask import render_template, request, jsonify # type: ignore
from checker.strategy_factory import StrategyFactory

def init_app(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/evaluate', methods=['POST'])
    def evaluate():
        password = request.form.get('password')
        strength_checker = StrategyFactory.get_strategy("strength")
        time_to_crack_calculator = StrategyFactory.get_strategy("time_to_crack")

        strength_level = strength_checker.evaluate(password)
        time_to_crack = time_to_crack_calculator.evaluate(password)

        return jsonify({
            'strength': strength_level,
            'time_to_crack': time_to_crack
        })
