var menuVM = new Vue({
    el: "#menu",
    data: {
        types: [
            "手机", "平板电脑", "笔记本", "摄影机"
        ],
        activeIndex: 0,
        subtypes: subtypes,
    },
    methods: {
        changeMenuType: function(index) {
            this.activeIndex = index;
        },
        typeLogo(index) {
            return 'type_' + index;
        },
    }
});