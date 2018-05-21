<template>
  <div>
    <NavHeader></NavHeader>
    <div>
      <table class="form-group">
        <tr>
          <th>Tag:</th>
          <th><input type="text" class="form-control" v-model="tag"></th>
        </tr>
        <br>
        <tr>
          <th>标记 </th>
          <th>
            <select class="form-control" multiple="multiple" v-model="check_articles">
              <option :value="article.id" v-for="article in articles">{{article.title}}</option>
            </select>
          </th>
        </tr>
        <br>
        <tr>
          <th>提交</th>
          <th>
            <button class="btn btn-danger" @click="submit">submit</button>
          </th>
        </tr>
      </table>
      <br>

    </div>
  </div>
</template>

<script>
  import NavHeader from '@/components/index/NavHeader'

  export default {
    name: "NewTag",
    data(){
      return {
        tag: '',
        articles: '',
        check_articles: []
      }
    },
    mounted(){
      this.$axios.get(process.env.API_HOST + '/api/article_titles', {headers: {'Authorization': 'Bearer '+ this.getCookie('token')}})
        .then(response => {
          this.articles = response.data.articles
        })
    },
    components: {NavHeader},
    methods: {
      submit: function () {
        this.$axios.post(process.env.API_HOST + '/api/new_tag', {'tag': this.tag, 'articles': this.check_articles}, {headers: {'Authorization': 'Bearer '+ this.getCookie('token')}})
          .then(response => {
            if (response.status === 200){
              alert('新建标签成功')
            }else{
               alert('新建标签失败, 请重新尝试')
            }
          })
      }
    }
  }
</script>

<style scoped>

</style>
