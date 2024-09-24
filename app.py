from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Placeholder for game state
game_state = {
    'board': [[None, None, None], [None, None, None], [None, None, None]],
    'turn': 'Player 1'
}

# Route for the game board
@app.route('/')
def index():
    return render_template('index.html', game_state=game_state)

# Route to make a move
@app.route('/move', methods=['POST'])
def make_move():
    data = request.get_json()
    x, y = data['x'], data['y']
    current_player = game_state['turn']
    
    if game_state['board'][x][y] is None:
        game_state['board'][x][y] = current_player
        game_state['turn'] = 'Player 2' if current_player == 'Player 1' else 'Player 1'
        return jsonify({'success': True, 'game_state': game_state})
    return jsonify({'success': False, 'message': 'Invalid move'})

if __name__ == '__main__':
    app.run(debug=True)
