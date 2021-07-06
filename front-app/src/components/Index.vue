<template>
  <v-card class="mx-auto">
    <v-row>
      <v-col v-for="(item, i) in problems" :key="i" cols="10" style="margin: 2%">
        <v-card :color="white" light>
          <div class="d-flex flex-no-wrap justify-space-between">
            <div>
              <v-card-title class="headline" v-text="item.title"></v-card-title>
              <v-card-subtitle style="color:black">Ваш голос: {{ item.votes }}</v-card-subtitle>
              <v-card-subtitle>
                <v-expansion-panels v-model="panel" :disabled="disabled">
                  <v-expansion-panel>
                    <v-expansion-panel-header>Подробности</v-expansion-panel-header>
                    <v-expansion-panel-content>
                      <b>Номер нерешенной проблемы:</b> {{ item.no_solved_task }}
                      <br />
                      <b>Глобальная экология:</b> {{ item.global_ecology_rating }}
                      <br />
                      <b>Глобальная экономика:</b> {{ item.global_economic_rating }}
                      <br />
                      <b>Глобальная бедность:</b> {{ item.global_poor_rating }}
                      <br />
                      <b>Глобальная нехватка продовольствия:</b> {{ item.global_food_rating }}
                      <br />
                    </v-expansion-panel-content>
                  </v-expansion-panel>
                </v-expansion-panels>
              </v-card-subtitle>
              <v-card-actions>
                <v-btn class="btn-success" style="color:white" text v-on:click="vote(item)">Отправить мой голос</v-btn>
              </v-card-actions>
            </div>
          </div>
        </v-card>
      </v-col>
    </v-row>
  </v-card>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      problems: [],
    };
  },
  created() {
    console.log("Здесь");
    this.all();
  },
  methods: {
    vote: function (problem) {
      if (confirm("Голос  " + problem.title)) {
        axios
          .post(`http://localhost:8000/api/vote/`, {
            problem_title: problem.title,
          })
          .then((response) => {
            console.log(response);
            alert("Вы проголлосовали за" + problem.title)
            this.all()
          })
          .catch(function (error) {
            if (error.response) {
              console.log(error);
              alert("Вы имеете право отдать свой голос только один раз");
            }
          });
      }
    },
    all: function () {
      console.log("Getting data");
      axios.get("http://localhost:8000/api/problem/", {
        auth: {
          username: "admin",
          password: "1234"
        }
      }).then((response) => {
        this.problems = response.data;
        console.log(response);
      });
    },
  },
};
</script>
