<template>
  <div>
    <div v-for="item in items">
      <h2>{{item.name}}</h2>
      <ol v-for="title in item.titles">
        <li>{{title.date}} => <router-link :to="{path: '/article/' + title['date'] + '/' + title['name']}">{{title.name}}</router-link></li>
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
      this.$axios.get('https://buglan.org/api/categories')
        .then(response => {
          this.items = response.data['category_json'];
          document.title = 'TimeAxis | BUGLAN';
        })
    }
  }
</script>

<style scoped>

</style>
