<template>
  <section id="articles">
    <ul>
      <li v-for="item in items" :key=item.id>
        <article>
          <h1>
            <router-link :to="{path: '/article/' + item['date'] + '/' + item.slug}">{{item.title}}</router-link>
          </h1>
          <p>{{item['date']}}</p>
          <div id="content" v-html="item.content" v-highlight></div>
          <br>
        </article>
      </li>
    </ul>
  </section>
</template>

<script>
import showdown from 'showdown'
export default {
  name: 'NavArticles',
  data () {
    return {
      items: []
    }
  },
  mounted () {
    this.$axios.get('/api/articles', { params: { page: this.$route.query.page } })
      .then(response => {
        this.items = response.data
        let converter = new showdown.Converter()
        this.items.forEach(item => {
          item.content = converter.makeHtml(item.raw_content + '...')
        })
      }).catch(response => {
        alert('出现错误请联系管理员')
      })
  },
  watch: {
    '$route' (to, from) {
      this.$axios.get('/api/articles', { params: { page: this.$route.query.page } })
        .then(response => {
          this.items = response.data
        })
    }
  }
}
</script>

<style scoped>

</style>
