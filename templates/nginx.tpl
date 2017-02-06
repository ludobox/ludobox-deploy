server {
        listen          80;
        server_name     {{ domain }};
        root            {{ root }};

        access_log      {{ log }}/access.log;
        error_log       {{ log }}/error.log;

        proxy_connect_timeout 75s;
        proxy_read_timeout 300s;

        location / {
                include proxy_params;
                proxy_pass http://unix://{{ socket }};
        }

}
