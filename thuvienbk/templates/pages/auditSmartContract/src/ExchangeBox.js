import React,{Component} from 'react';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemSecondaryAction from '@material-ui/core/ListItemSecondaryAction';
import ListItemText from '@material-ui/core/ListItemText';
import Checkbox from '@material-ui/core/Checkbox';
import { withStyles } from '@material-ui/core/styles';
import PropTypes from 'prop-types';
import Paper from '@material-ui/core/Paper';
import SendIcon from '@material-ui/icons/Send';
import IconButton from '@material-ui/core/IconButton';
import Typography from '@material-ui/core/Typography';
const styles = theme => ({
    root: {
        backgroundColor: theme.palette.background.paper,
        marginLeft: "auto",
        marginRight: "auto",
        width: "100%",
        marginTop: "20px",

    },
    list : {
        backgroundColor: theme.palette.background.paper,
        marginLeft: "auto",
        marginRight: "auto",
        width: "100%",
        height: "50px",
    }
});

class ExchangeBox extends Component{
    render(){
        const{classes} = this.props;

            return (
                <React.Fragment>
                    <Paper className={classes.root}>
                        <List dense className={classes.root}>
                            {this.props.userName && this.props.transactions !== [] && this.props.transactions.map((transaction,index) => (
                                <ListItem key={index} button>

                                    {this.props.userName === transaction.name && (<ListItemSecondaryAction>
                                        <IconButton aria-label="Comments" onClick={ () => this.props.sendTransaction(transaction.transaction)} >
                                            <SendIcon/>
                                        </IconButton>
                                    </ListItemSecondaryAction>)}
                                    <ListItemText >
                                            <Typography variant="title" gutterBottom>{`${transaction.transaction}`}</Typography>
                                    </ListItemText>


                                </ListItem>
                            ))}
                        </List>
                    </Paper>
                </React.Fragment>
            );
    }
}
ExchangeBox.propTypes = {
    classes: PropTypes.object.isRequired,
};
export default withStyles(styles)(ExchangeBox);