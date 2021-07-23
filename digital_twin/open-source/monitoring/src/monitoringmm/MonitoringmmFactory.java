/**
 */
package monitoringmm;

import org.eclipse.emf.ecore.EFactory;

/**
 * <!-- begin-user-doc -->
 * The <b>Factory</b> for the model.
 * It provides a create method for each non-abstract class of the model.
 * <!-- end-user-doc -->
 * @see monitoringmm.MonitoringmmPackage
 * @generated
 */
public interface MonitoringmmFactory extends EFactory {
	/**
	 * The singleton instance of the factory.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	MonitoringmmFactory eINSTANCE = monitoringmm.impl.MonitoringmmFactoryImpl.init();

	/**
	 * Returns a new object of class '<em>MO Agent</em>'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return a new object of class '<em>MO Agent</em>'.
	 * @generated
	 */
	MOAgent createMOAgent();

	/**
	 * Returns a new object of class '<em>MO Config</em>'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return a new object of class '<em>MO Config</em>'.
	 * @generated
	 */
	MOConfig createMOConfig();

	/**
	 * Returns a new object of class '<em>MO Property</em>'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return a new object of class '<em>MO Property</em>'.
	 * @generated
	 */
	MOProperty createMOProperty();

	/**
	 * Returns a new object of class '<em>MO Value</em>'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return a new object of class '<em>MO Value</em>'.
	 * @generated
	 */
	MOValue createMOValue();

	/**
	 * Returns the package supported by this factory.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the package supported by this factory.
	 * @generated
	 */
	MonitoringmmPackage getMonitoringmmPackage();

} //MonitoringmmFactory
