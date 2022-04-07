create database fazla_gida
    with owner postgres;

create table django_migrations
(
    id      bigserial,
    app     varchar(255)             not null,
    name    varchar(255)             not null,
    applied timestamp with time zone not null,
    primary key (id)
);

alter table django_migrations
    owner to postgres;

create table django_content_type
(
    id        serial,
    app_label varchar(100) not null,
    model     varchar(100) not null,
    primary key (id),
    constraint django_content_type_app_label_model_76bd3d3b_uniq
        unique (app_label, model)
);

alter table django_content_type
    owner to postgres;

create table auth_permission
(
    id              serial,
    name            varchar(255) not null,
    content_type_id integer      not null,
    codename        varchar(100) not null,
    primary key (id),
    constraint auth_permission_content_type_id_codename_01ab375a_uniq
        unique (content_type_id, codename),
    constraint auth_permission_content_type_id_2f476e4b_fk_django_co
        foreign key (content_type_id) references django_content_type
            deferrable initially deferred
);

alter table auth_permission
    owner to postgres;

create index auth_permission_content_type_id_2f476e4b
    on auth_permission (content_type_id);

create table auth_group
(
    id   serial,
    name varchar(150) not null,
    primary key (id),
    unique (name)
);

alter table auth_group
    owner to postgres;

create index auth_group_name_a6ea08ec_like
    on auth_group (name varchar_pattern_ops);

create table auth_group_permissions
(
    id            bigserial,
    group_id      integer not null,
    permission_id integer not null,
    primary key (id),
    constraint auth_group_permissions_group_id_permission_id_0cd325b0_uniq
        unique (group_id, permission_id),
    constraint auth_group_permissions_group_id_b120cbf9_fk_auth_group_id
        foreign key (group_id) references auth_group
            deferrable initially deferred,
    constraint auth_group_permissio_permission_id_84c5c92e_fk_auth_perm
        foreign key (permission_id) references auth_permission
            deferrable initially deferred
);

alter table auth_group_permissions
    owner to postgres;

create index auth_group_permissions_group_id_b120cbf9
    on auth_group_permissions (group_id);

create index auth_group_permissions_permission_id_84c5c92e
    on auth_group_permissions (permission_id);

create table auth_user
(
    id           serial,
    password     varchar(128)             not null,
    last_login   timestamp with time zone,
    is_superuser boolean                  not null,
    username     varchar(150)             not null,
    first_name   varchar(150)             not null,
    last_name    varchar(150)             not null,
    email        varchar(254)             not null,
    is_staff     boolean                  not null,
    is_active    boolean                  not null,
    date_joined  timestamp with time zone not null,
    primary key (id),
    unique (username)
);

alter table auth_user
    owner to postgres;

create index auth_user_username_6821ab7c_like
    on auth_user (username varchar_pattern_ops);

create table auth_user_groups
(
    id       bigserial,
    user_id  integer not null,
    group_id integer not null,
    primary key (id),
    constraint auth_user_groups_user_id_group_id_94350c0c_uniq
        unique (user_id, group_id),
    constraint auth_user_groups_user_id_6a12ed8b_fk_auth_user_id
        foreign key (user_id) references auth_user
            deferrable initially deferred,
    constraint auth_user_groups_group_id_97559544_fk_auth_group_id
        foreign key (group_id) references auth_group
            deferrable initially deferred
);

alter table auth_user_groups
    owner to postgres;

create index auth_user_groups_user_id_6a12ed8b
    on auth_user_groups (user_id);

create index auth_user_groups_group_id_97559544
    on auth_user_groups (group_id);

create table auth_user_user_permissions
(
    id            bigserial,
    user_id       integer not null,
    permission_id integer not null,
    primary key (id),
    constraint auth_user_user_permissions_user_id_permission_id_14a6b632_uniq
        unique (user_id, permission_id),
    constraint auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id
        foreign key (user_id) references auth_user
            deferrable initially deferred,
    constraint auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm
        foreign key (permission_id) references auth_permission
            deferrable initially deferred
);

alter table auth_user_user_permissions
    owner to postgres;

create index auth_user_user_permissions_user_id_a95ead1b
    on auth_user_user_permissions (user_id);

create index auth_user_user_permissions_permission_id_1fbb5f2c
    on auth_user_user_permissions (permission_id);

create table django_session
(
    session_key  varchar(40)              not null,
    session_data text                     not null,
    expire_date  timestamp with time zone not null,
    primary key (session_key)
);

alter table django_session
    owner to postgres;

create index django_session_session_key_c0390e0f_like
    on django_session (session_key varchar_pattern_ops);

create index django_session_expire_date_a5c62663
    on django_session (expire_date);

create table "FazlaGidaChallenge_category"
(
    id   bigserial,
    name varchar(250) not null,
    slug varchar(50)  not null,
    primary key (id),
    constraint "FazlaGidaChallenge_category_name_b5a9859a_uniq"
        unique (name)
);

alter table "FazlaGidaChallenge_category"
    owner to postgres;

create index "FazlaGidaChallenge_category_slug_b9ad752d"
    on "FazlaGidaChallenge_category" (slug);

create index "FazlaGidaChallenge_category_slug_b9ad752d_like"
    on "FazlaGidaChallenge_category" (slug varchar_pattern_ops);

create table "FazlaGidaChallenge_store"
(
    id   bigserial,
    name varchar(255) not null,
    slug varchar(50)  not null,
    primary key (id)
);

alter table "FazlaGidaChallenge_store"
    owner to postgres;

create index "FazlaGidaChallenge_store_slug_6c2d8783"
    on "FazlaGidaChallenge_store" (slug);

create index "FazlaGidaChallenge_store_slug_6c2d8783_like"
    on "FazlaGidaChallenge_store" (slug varchar_pattern_ops);

create table "FazlaGidaChallenge_profile"
(
    id      bigserial,
    role    varchar(50) not null,
    user_id integer     not null,
    primary key (id),
    unique (user_id),
    constraint "FazlaGidaChallenge_profile_user_id_54e72c98_fk_auth_user_id"
        foreign key (user_id) references auth_user
            deferrable initially deferred
);

alter table "FazlaGidaChallenge_profile"
    owner to postgres;

create table "FazlaGidaChallenge_product"
(
    id          bigserial,
    name        varchar(255)             not null,
    slug        varchar(50)              not null,
    price       numeric(10, 2)           not null,
    category_id bigint                   not null,
    store_id    bigint                   not null,
    created_at  timestamp with time zone not null,
    description varchar(600)             not null,
    primary key (id),
    constraint "FazlaGidaChallenge_p_category_id_5a16fe86_fk_FazlaGida"
        foreign key (category_id) references "FazlaGidaChallenge_category"
            deferrable initially deferred,
    constraint "FazlaGidaChallenge_p_store_id_2103a859_fk_FazlaGida"
        foreign key (store_id) references "FazlaGidaChallenge_store"
            deferrable initially deferred
);

alter table "FazlaGidaChallenge_product"
    owner to postgres;

create index "FazlaGidaChallenge_product_slug_0ac3c21b"
    on "FazlaGidaChallenge_product" (slug);

create index "FazlaGidaChallenge_product_slug_0ac3c21b_like"
    on "FazlaGidaChallenge_product" (slug varchar_pattern_ops);

create index "FazlaGidaChallenge_product_category_id_5a16fe86"
    on "FazlaGidaChallenge_product" (category_id);

create index "FazlaGidaChallenge_product_store_id_2103a859"
    on "FazlaGidaChallenge_product" (store_id);

create table django_admin_log
(
    id              serial,
    action_time     timestamp with time zone not null,
    object_id       text,
    object_repr     varchar(200)             not null,
    action_flag     smallint                 not null,
    change_message  text                     not null,
    content_type_id integer,
    user_id         integer                  not null,
    primary key (id),
    constraint django_admin_log_content_type_id_c4bce8eb_fk_django_co
        foreign key (content_type_id) references django_content_type
            deferrable initially deferred,
    constraint django_admin_log_user_id_c564eba6_fk_auth_user_id
        foreign key (user_id) references auth_user
            deferrable initially deferred
);

alter table django_admin_log
    owner to postgres;

create index django_admin_log_content_type_id_c4bce8eb
    on django_admin_log (content_type_id);

create index django_admin_log_user_id_c564eba6
    on django_admin_log (user_id);

alter table django_admin_log
    add constraint django_admin_log_action_flag_check
        check (action_flag >= 0);

create table "FazlaGidaChallenge_product_favorite"
(
    id         bigserial,
    product_id bigint  not null,
    user_id    integer not null,
    primary key (id),
    constraint "FazlaGidaChallenge_produ_product_id_user_id_f19d89d1_uniq"
        unique (product_id, user_id),
    constraint "FazlaGidaChallenge_p_product_id_1354b662_fk_FazlaGida"
        foreign key (product_id) references "FazlaGidaChallenge_product"
            deferrable initially deferred,
    constraint "FazlaGidaChallenge_p_user_id_bfa669e6_fk_auth_user"
        foreign key (user_id) references auth_user
            deferrable initially deferred
);

alter table "FazlaGidaChallenge_product_favorite"
    owner to postgres;

create index "FazlaGidaChallenge_product_favorite_product_id_1354b662"
    on "FazlaGidaChallenge_product_favorite" (product_id);

create index "FazlaGidaChallenge_product_favorite_user_id_bfa669e6"
    on "FazlaGidaChallenge_product_favorite" (user_id);

create table "FazlaGidaChallenge_store_favorite"
(
    id       bigserial,
    store_id bigint  not null,
    user_id  integer not null,
    primary key (id),
    constraint "FazlaGidaChallenge_store_store_id_user_id_e725f9e4_uniq"
        unique (store_id, user_id),
    constraint "FazlaGidaChallenge_s_store_id_0ce709b6_fk_FazlaGida"
        foreign key (store_id) references "FazlaGidaChallenge_store"
            deferrable initially deferred,
    constraint "FazlaGidaChallenge_s_user_id_f4fe3967_fk_auth_user"
        foreign key (user_id) references auth_user
            deferrable initially deferred
);

alter table "FazlaGidaChallenge_store_favorite"
    owner to postgres;

create index "FazlaGidaChallenge_store_favorite_store_id_0ce709b6"
    on "FazlaGidaChallenge_store_favorite" (store_id);

create index "FazlaGidaChallenge_store_favorite_user_id_f4fe3967"
    on "FazlaGidaChallenge_store_favorite" (user_id);


