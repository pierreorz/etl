export function localGet (key:string) {
    const value = window.localStorage.getItem(key)
    try {
      
      return JSON.parse(window.localStorage.getItem(key)||'{}')
    } catch (error) {
      return value
    }
  }
  
  export function localSet (key:string, value:string) {
    window.localStorage.setItem(key, JSON.stringify(value))
  }
  
  export function localRemove (key:string) {
    window.localStorage.removeItem(key)
  }
  