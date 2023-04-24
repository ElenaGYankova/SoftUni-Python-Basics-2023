movie_name = input()
seasons_count = int(input())
episodes_count = int(input())
single_episode_time = float(input())

episode_real_time = 1.2 * single_episode_time
additional_time_for_last_episode = 10

season_time = episode_real_time * episodes_count + additional_time_for_last_episode
total_time = int(seasons_count * season_time)

print(f"Total time needed to watch the {movie_name} series is {total_time} minutes.")
