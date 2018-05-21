<template>
  <div>
    <div v-for="item in items">
      <h2>{{item.name}}</h2>
      <ol>
          <template v-for="title in item.titles">
        <li>{{title.date}} => <router-link :to="{path: '/article/' + title['date'] + '/' + title['name']}">{{title.name}}</router-link></li>
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
          this.items = response.data['category_json'];
          document.title = 'TimeAxis | BUGLAN';
        })
    }
  }
</script>

<style scoped>

</style>
