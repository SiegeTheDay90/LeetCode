class EventEmitter {
    constructor(){
        this.events = {};
    }
  
    subscribe(event, cb) {
      this.events[event] ||= new Set()
      this.events[event].add(cb)
      return {
          unsubscribe: () => {
            this.events[event].delete(cb)
          }
      };
    }
  
    emit(event, args = []) {
      const results = []
      this.events[event]?.forEach((cb) =>{
        results.push(cb(...args))
      })
      return results
    }
  }