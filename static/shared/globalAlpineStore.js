document.addEventListener('alpine:init', () => {
    Alpine.store('tabs', {
        current: 'first',
        items: [],
        add(tab) {
            if (!this.items.some(item => item.id === tab.id)) {
                this.items.push(tab)
            }
            this.setCurrent(tab.id);
        },        
        setCurrent(id) {
            if (!id) {
                this.current = ''
                return
            }
            this.current = this.items.find(item => item.id === id).id
        },
        removeTab (id) {
            if (!id) {
                return
            }
            let itemIndex = 0;
            const element = document.getElementById(id);
            element.remove();
            this.items = this.items.filter((item, index) => {
                itemIndex = index
                return item.id !== id})

            if(!itemIndex){
                this.setCurrent('')
            }
            else if (id === this.current) {
                this.setCurrent(this.items[itemIndex-1]?.id)
            }


            
        },
        tabExisted(id) {
            return this.items.some(item => item.id === id)
        }
    })
})