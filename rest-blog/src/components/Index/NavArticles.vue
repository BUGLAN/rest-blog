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
      this.$axios.get('http://127.0.0.1:5000/api/articles', {params: {page: this.$route.query.page}})
        .then(response => {
          this.items = response.data['articles'];
          console.log(this.items)
        }).catch(response => {
        console.log(response.status)
      })
    },
    watch: {
      '$route'(to, from) {
        this.$axios.get('http://127.0.0.1:5000/api/articles', {params: {page: this.$route.query.page}})
          .then(response => {
            this.items = response.data['articles'];
          })
      }
    }
  }
</script>

<style scoped>

</style>
