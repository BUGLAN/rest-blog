<template>
  <table class="form-group">
    <tr>
      <th>Tag:</th>
      <th><input type="text" class="form-control" v-model="name"></th>
    </tr>
    <br>
    <br>
    <tr>
      <th>提交</th>
      <th>
        <button class="btn btn-danger" @click="submit">submit</button>
      </th>
    </tr>
  </table>
</template>

<script>
export default {
  name: 'EditorTag',
  data () {
    return {
      name: '',
      tag_id: ''
    }
  },
  mounted () {
    this.name = this.$route.params.name
    this.$axios.get('/api/tag', { params: { 'name': this.name } }, { headers: { 'Authorization': 'Bearer ' + this.getCookie('token') } })
      .then(response => {
        this.tag_id = response.data.id
        document.title = '编辑 ' + this.name + ' | BUGLAN'
      })
  },
  methods: {
    submit: function () {
      this.$axios.put('/api/tag', { 'id': this.tag_id, 'name': this.name }, { headers: { 'Authorization': 'Bearer ' + this.getCookie('token') } })
        .then(response => {
          if (response.status === 200) {
            alert('修改成功')
          }
        })
    }
  }
}
</script>

<style scoped>

</style>
