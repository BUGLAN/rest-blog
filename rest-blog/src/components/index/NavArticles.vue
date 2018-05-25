<template>
  <section id="articles">
    <ul>
      <li v-for="item in items">
        <article>
          <h1>
            <router-link :to="{path: '/article/' + item['date'] + '/' + item.slug}">{{item.title}}</router-link>
          </h1>
          <p>{{item['date']}}</p>
          <div class="content" v-html="item['content']"></div>
          <br>
        </article>
      </li>
    </ul>
  </section>
</template>

<script>
  export default {
    name: "NavArticles",
    data() {
      return {
        items: []
      }
    },
    mounted() {
      this.$axios.get(process.env.API_HOST + '/api/articles', {params: {page: this.$route.query.page}})
        .then(response => {
          this.items = response.data;
        }).catch(response => {
        alert("出现错误请联系管理员")
      })
    },
    watch: {
      '$route'(to, from) {
        this.$axios.get(process.env.API_HOST + '/api/articles', {params: {page: this.$route.query.page}})
          .then(response => {
            this.items = response.data;
          })
      }
    }
  }
</script>

<style scoped>

</style>
