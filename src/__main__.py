

if __name__ == "__main__":
    engine = Engine()
    engine.load('config')

    room = engine.get_random_room(tags=None, args=None)
    engine.set_room(room)

    while True:
        engine.run_game()
