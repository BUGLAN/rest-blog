const Test = Vue.component({
    props:['test'],
    'test-blog': {
        template: '<template>\n' +
        '  <div >\n' +
        '    <div>\n' +
        '      <p>{{test}}</p>\n' +
        '      </div>\n' +
        '    </div>\n' +
        '  </div>\n' +
        '</template>'
    }
})

const routers = new VueRouter({
    mode: 'history',
    routes: [
        {
            path: '/test',
            name: 'Test',
            component: Test
        }
    ]
})

new Vue({
    el: '#app1',
    data(){
        return {
            test: ''
        }
    },
    mounted() {
        axios.get('/api/articles')
            .then(response => {
                this.test = response.data['msg']
            })
    },
    router: routers,
    method: {
        do_test: function () {
            this.$router.push({name: 'Test'})
        }
    },
    components: {
        props: ['test'],
        'for-test': {
            template: '<h1><p @click="do_test()" >{{test}}</p></h1>'

        }
    }
})