const setSession = (username, userId, token) => {
    sessionStorage.setItem('userame', username);
    sessionStorage.setItem('userId', userId);
    sessionStorage.setItem('token', token);
};

const endSession = () => {
    sessionStorage.clear()
};

const getUsername = () => sessionStorage.getItem('username');
const getUserId = () => sessionStorage.getItem('userId');
const getToken = () => sessionStorage.getItem('token');