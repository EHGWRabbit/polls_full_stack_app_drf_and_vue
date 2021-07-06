<template>
  <v-container>
    <v-form @submit="create" ref="form" lazy-validation>
      <v-text-field v-model="admin_id" :counter="250" label="Идентификатор" required></v-text-field>
      <v-text-field v-model="admin_password" label="Пароль" type="password" required></v-text-field>
      <v-text-field v-model="problem.title" :counter="250" label="Название проблемы" required></v-text-field>
      <v-text-field
        v-model="problem.no_solved_tasks"
        label="Номер проблемы"
        type="number"
      ></v-text-field>
      <v-select
        v-model="problem.global_ecology_rating"
        :items="ratings"
        :rules="[v => !!v || 'Рэйтинг глобальной экологии']"
        label="Экологический рэйтинг"
        required
      ></v-select>
      <v-select
        v-model="problem.global_economic_rating"
        :items="ratings"
        :rules="[v => !!v || 'Рэйтинг глобальной экономики']"
        label="Экономический рэйтинг"
        required
      ></v-select>
      <v-select
        v-model="problem.global_poor_rating"
        :items="ratings"
        :rules="[v => !!v || 'Глобальная проблема бедности']"
        label="Рэйтинг глобальной бедности"
        required
      ></v-select>
      <v-select
        v-model="problem.global_food_rating"
        :items="ratings"
        :rules="[v => !!v || 'Глобальная продовольственная проблема']"
        label="Рэйтинг глобальной продовольственной проблемы"
        required
      ></v-select>
      <v-btn color="primary" type="submit">Отправить</v-btn>
    </v-form>
  </v-container>
</template>

<script>

import axios from "axios";
export default {
  data() {
    return {
      ratings: [1, 2, 3, 4, 5],
      num: 1,
        problem: {
        title: "",
        no_solved_tasks: 0,
        global_ecology_rating: 1,
        global_economic_rating: 1,
        global_poor_rating: 1,
        global_food_rating: 1
      },
      admin_id: "1234",
      admin_password: "admin",
      submitted: false,
    };
  },
  methods: {
    create: function () {
      axios
        .post("http://127.0.0.1:8000/api/cry/", this.problem, {
          auth: {
            username: this.admin_id,
            password: this.admin_password,
          },
        })
        .then((response) => {
          console.log(response);
          alert("Регистрация прошла успешно!");
          this.$router.push("/");
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
