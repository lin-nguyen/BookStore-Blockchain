import React, { Component } from 'react';
import Typography from '@material-ui/core/Typography';
import { withStyles } from '@material-ui/core/styles';
import PropTypes from 'prop-types';
import Paper from '@material-ui/core/Paper';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import Review from './Review.js';
import axios from 'axios';
import Link from '@material-ui/core/Link';
import ExchangeBox from './ExchangeBox.js';
import Web3 from 'web3';
const web3 = new Web3(new Web3.providers.WebsocketProvider("ws://localhost:7545"));

const styles = theme =>( {
    root: {
        margin : "auto",
        marginTop : theme.spacing.unit * 10,
        paddingTop: theme.spacing.unit * 2,
        paddingBottom: theme.spacing.unit * 2,
        paddingLeft: theme.spacing.unit * 2,
        paddingRight: theme.spacing.unit * 2,
        width : "95%"
    },
    container: {
        display: 'inline',
        flexWrap: 'wrap',
    },
    textField: {
        marginLeft: theme.spacing.unit,
        marginRight: theme.spacing.unit,
        width: "100%"
    },
    layoutTransaction : {

        paddingTop: theme.spacing.unit * 2,
        paddingBottom: theme.spacing.unit * 2,
        paddingLeft: theme.spacing.unit * 2,
        paddingRight: theme.spacing.unit * 2,
        marginTop : theme.spacing.unit*3,
        marginBottom : theme.spacing.unit*3,
        marginLeft : "20%",
        marginRight : "20%",

    },
    button: {
        margin: theme.spacing.unit,
    },
    fab: {
        margin: theme.spacing.unit*2,
    },
    rightIcon: {
        margin: theme.spacing.unit,
    },
});
const IP_address = "172.28.247.94";
const escrowContract = new web3.eth.Contract([{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"ether_amount","type":"uint256"}],"name":"sendeth","outputs":[],"payable":true,"stateMutability":"payable","type":"function","funcName":"sendeth(address,address,uint256)","signature":"0x5ff49ce3"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_tokenAddress","type":"address"},{"name":"token_amount","type":"uint256"}],"name":"sendtoken","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function","funcName":"sendtoken(address,address,address,uint256)","signature":"0xe5a1f214"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor","signature":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"name":"number_line","type":"uint256"}],"name":"check","type":"event","funcName":"check(uint256)","signature":"0x5f72f450c381493c8b88f0bcbf2bbe88a1ad56665696daa7cb7349917afdd320"}]
    ,"0xE5a1EA9bEEd9c050ad16EB656F21612309DF2aD9");

const tokenContract = new web3.eth.Contract([{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function","funcName":"name()","signature":"0x06fdde03"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},
        {"name":"tokens","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function","funcName":"approve(address,uint256)","signature":"0x095ea7b3"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"tokens","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function","funcName":"transferFrom(address,address,uint256)","signature":"0x23b872dd"},{"constant":true,"inputs":[],
    "name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function","funcName":"decimals()","signature":"0x313ce567"},{"constant":true,"inputs":[{"name":"_tokenOwner","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function","funcName":"balanceOf(address)","signature":"0x70a08231"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function","funcName":"symbol()","signature":"0x95d89b41"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"tokens","type":"uint256"}],
    "name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function","funcName":"transfer(address,uint256)","signature":"0xa9059cbb"},{"constant":true,"inputs":[{"name":"tokenOwner","type":"address"},{"name":"spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function","funcName":"allowance(address,address)","signature":"0xdd62ed3e"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor","signature":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"tokens","type":"uint256"}],"name":"Transfer","type":"event",
    "funcName":"Transfer(address,address,uint256)","signature":"0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"},
    {"anonymous":false,"inputs":[{"indexed":true,"name":"tokenOwner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,
        "name":"tokens","type":"uint256"}],"name":"Approval","type":"event","funcName":"Approval(address,address,uint256)","signature":"0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925"}],"0xb4D6d66d76896D99F0A52c8d6C010cEb401F9d5A");

tokenContract.events.allEvents((error, event) => {
    if (error) {
        console.error(error);
        return false;
    }

    console.log(event);
});

escrowContract.events.allEvents((error, event) => {
    if (error) {
        console.error(error);
        return false;
    }

    console.log(event);
});

class mainPage extends Component{
    constructor(props){
        super(props);
        this.state = {
            contextTransaction : '',
            responseState : [],
            transactions : [],
            userName : '',
            tokenAddress : '',
            checkValidate : '' ,
            disabledSend: true,
        };
        const myContract = '';
    };


    componentDidMount() {
        setInterval(() => {
            axios.get(`http://${IP_address}:3001/refresh`).then(res => {
                res =res.data;
                if( res.length > this.state.transactions.length) {
                    console.log(res.length + " " + this.state.transactions.length);

                    this.setState({"transactions": res});

                    // console.log(this.state.transactions);
                }
            })
        },1000);
    }

    callAjax_sendTransaction = () => {
        alert("Transfer success");
        // if (this.state.contextTransaction !== "" && this.state.sender !== "") {
        //     axios.post(`http://${IP_address}:3001/sendTransaction`, {
        //             senderName : this.state.userName,
        //             transaction: this.state.contextTransaction
        //     }).then(res => {
        //         console.log(res.data);
        //     })
        // }
    };
	
    callAjax_backtohome = () => {
    window.open('http://127.0.0.1:8000/','_self');

}
    callAjax_validate = () => {
    	if(true){
    		this.setState({"disabledSend":false });
    	}
        else{
            alert("Smart Contract is not trusted");
        }


            // axios.post(`http://${IP_address}:3001/validate`, {
            //     transactions : this.state.transactions.map(transaction => transaction.transaction).join("")
            // }).then(res => {
            //     console.log(res.data);
            //     this.setState({"responseState": res.data});
            // })
    };

    sendethFunc = (_from, _to, amount) => {
        console.log("send eth " + _from + " " + _to + " " + amount);
        escrowContract.methods.sendeth(_from,_to,web3.utils.toWei(amount,'ether').toString())
            .send({from : _from, gasPrice : "100000000000", gas : "4712388", value : web3.utils.toWei(amount,'ether').toString()})
            .on('transactionHash', (hash) => {
                console.log(hash);
            })
    };

    sendtokenFunc= (_from, _to, token_address , amount) => {
        console.log("send token " + _from + " " + _to + " "+token_address +" " + amount);

        escrowContract.methods.sendtoken(_from,_to,token_address, amount)
            .send({from : _from, gasPrice : "100000000000", gas : "4712388"})
            .on('transactionHash', (hash) => {
                console.log(hash);
            })
    };

// # {
//     #     transaction : {
//         #         "text" : ...,
//         #         "type" : ...,
//         #         "_from" : ...,
//         #         "_to" : ...,
//         #         "address_token" : ...,
//         #         "amount" : ...,
//         #     },
//     #     'account_state' : functools.reduce
// # }

    sendTransaction = (transaction_1) => {
        let transaction;
        console.log("aaaaaa");
        if (this.state.responseState !== '') {

            let responseState = this.state.responseState;
            transaction = responseState.filter( transac => {
                console.log(transac.transaction.text,transaction_1.slice(0,transaction_1.length-1));
                return transac.transaction.text === transaction_1.slice(0,transaction_1.length-1); });
            // console.log(JSON.stringify(transaction));

            transaction = transaction[0].transaction ;
            // console.log("#"+ transaction);
            if (transaction.type === "sendeth") {
                this.sendethFunc(transaction._from , transaction._to, transaction.amount);
            }
            else if (transaction.type === "sendtoken") {
                console.log(transaction);
                // token thừa , và khaognr trống , phải bỏ đi
                this.sendtokenFunc(transaction._from , transaction._to, transaction.address_token.slice(1,transaction.address_token.length-1), transaction.amount);
            }
            else{
                console.log("line 161");
            }
        }
    };

    sendToken = () => {

        // escrowContract.methods.sendeth("0x6462a0ab9e11F8B47ee153e46E4c3f5f9593ece0","0x8D26738a7bECC37ed5D100639d080FB9835E1008",web3.utils.toWei("1","ether").toString())
        //     .send({from : "0x6462a0ab9e11F8B47ee153e46E4c3f5f9593ece0", gasPrice : "100000000000", gas : "4712388", value : web3.utils.toWei("1","ether").toString()})
        //     .on('transactionHash', (hash) => {
        //         console.log(hash);
        //     });

        // escrowContract.methods.sendtoken("0x8D26738a7bECC37ed5D100639d080FB9835E1008","0x6462a0ab9e11F8B47ee153e46E4c3f5f9593ece0","0xb4D6d66d76896D99F0A52c8d6C010cEb401F9d5A", "10000")
        //     .send({from : "0x8D26738a7bECC37ed5D100639d080FB9835E1008", gasPrice : "100000000000", gas : "3200000"})
        //     .then(res => {
        //         console.log("@@@"+JSON.stringify(res));
        //     })
        //     .catch(error  => {
        //         console.log(error);
        //     });

        // tokenContract.methods.balanceOf("0x6462a0ab9e11F8B47ee153e46E4c3f5f9593ece0")
        //     .call({from: "0x6462a0ab9e11F8B47ee153e46E4c3f5f9593ece0", gasPrice: "100000000000", gas: "4712388"})
        //     .then( res => {
        //         console.log("# " +res);
        //     });

        // tokenContract.methods.transfer("0x8D26738a7bECC37ed5D100639d080FB9835E1008", "100000000")
        //     .send({from: "0x87616A71Ae0B412e402D846fae89dBF57a32031e", gasPrice: "100000000000", gas: "4712388"})
        //     .on('transactionHash', (hash) => {
        //         console.log(hash);
        //     })


        // tokenContract.methods.approve("0xE5a1EA9bEEd9c050ad16EB656F21612309DF2aD9","10000")
        //     .send({from: "0x8D26738a7bECC37ed5D100639d080FB9835E1008", gasPrice: "100000000000", gas: "4712388"})
        //     .then( res => {
        //         console.log("# " +res);
        //     });

        // tokenContract.methods.allowance("0x8D26738a7bECC37ed5D100639d080FB9835E1008","0xE5a1EA9bEEd9c050ad16EB656F21612309DF2aD9")
        //     .call({from: "0x8D26738a7bECC37ed5D100639d080FB9835E1008", gasPrice: "100000000000", gas: "4712388"})
        //     .then( res => {
        //         console.log("# " +res);
        //     });
        //
        // tokenContract.methods.transferFrom("0x8D26738a7bECC37ed5D100639d080FB9835E1008","0x30D75Ed05305A0EEB230f2f8adDE680897751fF0","10000")
        //     .send({from: "0x30D75Ed05305A0EEB230f2f8adDE680897751fF0", gasPrice: "100000000000", gas: "4712388"})
        //     .then( res => {
        //         console.log("# " +res);
        //     });

        // web3.eth.sendTransaction({
        //     from: "0x87616A71Ae0B412e402D846fae89dBF57a32031e",
        //     to: "0xb71381649157D04DDAde46263498218CCDA74C54",
        //
        //     value: web3.utils.toWei("3","ether")
        // })
    };
    handleChange = prop => event => {
            this.setState({[prop] : event.target.value});
    };
    render() {
        const {classes} = this.props;
        return (
            <React.Fragment>
                <Paper className={classes.root}>
                    <Typography component="h3" variant="h3" gutterBottom>
                        Smart Contracts Audit
                    </Typography>
                    <form className={classes.container}>
                        <TextField	
                            id="userName"
                            label="Smart Contract"
                            value={this.state.userName}
                            onChange={this.handleChange('userName')}
                            className={classes.textField}
                            margin="normal"
                            variant="outlined"
                        />
                        <ExchangeBox transactions={this.state.transactions}  userName={this.state.userName} sendTransaction={this.sendTransaction}/>
                        <TextField
                            id="Transaction"
                            label="Transaction"
                            value={"sendether(User, Admin, 10) -> sendtoken(Admin, User, 10)"}
                            onChange={this.handleChange('contextTransaction')}
                            className={classes.textField}
                            margin="normal"
                            variant="outlined"
                        />
                        <br/>
                        <Button variant="contained" color="primary" className={classes.button}
                                onClick={this.callAjax_validate}>
                            Request Audit
                        </Button>

                        <Button disabled={this.state.disabledSend} variant="contained" color="primary" className={classes.button}
                                onClick={this.callAjax_sendTransaction}>
                            send Transaction
                        </Button>
	
                        <Button variant="contained" color="#3FFFF" className={classes.button}
				 onClick={this.callAjax_backtohome}>
                            Back to HomePage
                        </Button>

                        {/*<Button variant="contained" color="primary" className={classes.button}*/}
                                {/*onClick={this.sendToken}>*/}
                            {/*watch*/}
                        {/*</Button>*/}

                        {/*<Button variant="contained" color="primary" className={classes.button}*/}
                                {/*onClick={this.sendToken}>*/}
                            {/*send token*/}
                        {/*</Button>*/}
                    </form>
                    <Review responseState={this.state.responseState}/>
                </Paper>
            </React.Fragment>
        );
    }
}
mainPage.propTypes = {
    classes: PropTypes.object.isRequired,
};
export default withStyles(styles)(mainPage);
