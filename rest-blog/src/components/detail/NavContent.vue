<template>
  <section id="article">
    <ul>
      <li>
        <article>
          <h1>{{item.title}}</h1>
          <p>{{item.date}}</p>

          <div id="content" v-html="item.content" v-highlight></div>
          <p><router-link :to="{path: '/article/' + item.date + '/' + item.slug + '/' + 'editor'}">Editor</router-link></p>
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
    this.$axios.get(process.env.API_HOST + '/api/mega_article', {params: {slug: this.$route.params.name}})
      .then(response => {
        let converter = new showdown.Converter();
        this.item = response.data;
        //this.item.content = converter.makeHtml(this.item.content);
        document.title = this.item.title + ' | BUGLAN'
      }).catch(response => {
        console.log(response)
      })
  },
}
</script>
<style>
</style>
