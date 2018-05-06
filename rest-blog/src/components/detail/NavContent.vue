<template>
  <section id="articles">
    <ul>
      <li>
        <article>
          <h1>{{item.title}}</h1>
          <p>{{item.date}}</p>
          <div class="content" v-html="item.content"></div>
          <p><router-link :to="{path: '/article/' + item.date + '/' + item.title + '/' + 'editor'}">Editor</router-link></p>
        </article>
      </li>
    </ul>
  </section>
</template>

<script>
  export default {
    name: "Detail",
    data() {
      return {item: []}
    },
    mounted() {
      this.$axios.get('http://127.0.0.1:5000/api/article', {params: {title: this.$route.params.name}})
        .then(response => {
          this.item = response.data.article
        }).catch(response => {
          console.log(response.status)
      })
    }
  }
</script>

<style scoped>

</style>
