use friendships;
select users.first_name, users.last_name, user2.first_name as friend_first_name, user2.last_name as friend_last_name from users
left join friendships on users.id = friendships.user_id
left join users as user2 on friendships.friend_id = user2.id;
