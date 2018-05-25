<template>
  <div>
    <div v-for="item in items">
      <h2>{{item.name}}</h2>
      <ol>
          <template v-for="article in item.articles">
        <li>{{article.date}} => <router-link :to="{path: '/article/' +
                article['date'] + '/' + article['slug']}">{{article.title}}</router-link></li>
          </template>
      </ol>
    </div>
  </div>
</template>

<script>
  // 获取所有标签
  export default {
    name: "TimeAxis",
    data(){
      return {
        items: ''
      }
    },
    mounted() {
      this.$axios.get(process.env.API_HOST + '/api/categories')
        .then(response => {
          this.items = response.data;
          document.title = 'TimeAxis | BUGLAN';
        })
    }
  }
</script>

<style scoped>

</style>
