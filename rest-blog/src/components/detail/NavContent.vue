<template>
  <section id="article">
    <ul>
      <li>
        <article>
          <h1>{{item.title}}</h1>
          <p>{{item.date}}</p>

          <div id="content" v-html="item.content" v-highlight></div>
          <p><router-link :to="{path: '/article/' + item.date + '/' + item.title + '/' + 'editor'}">Editor</router-link></p>
        </article>
      </li>
    </ul>
  </section>
</template>

<script>
  import showdown from 'showdown'
  import hljs  from 'highlight.js'
  export default {
    name: "Detail",
    data() {
      return {item: []}
    },
    mounted() {
      this.$axios.get('http://127.0.0.1:5000/api/article', {params: {title: this.$route.params.name}})
        .then(response => {
           let converter = new showdown.Converter()
          this.item = response.data.article
          this.item.content = converter.makeHtml(this.item.content)
        }).catch(response => {
          console.log(response.status)
      })
    },
  }
</script>
<style>
</style>
